# -*- coding: utf-8 -*-

from __future__ import absolute_import

from copy import deepcopy

from docutils import nodes, utils
from docutils.core import publish_parts
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.body import CodeBlock
from docutils.parsers.rst.roles import register_canonical_role, set_classes
from docutils.utils.code_analyzer import Lexer, LexerError
from docutils.writers.html4css1 import HTMLTranslator, Writer

from mynt.base import Parser as _Parser


def code_role(role, rawtext, text, lineno, inliner, options = {}, content = []):
    set_classes(options)
    language = options.get('language', '')
    classes = []
    
    if 'classes' in options:
        classes.extend(options['classes'])
    
    if language and language not in classes:
        classes.append(language)
    
    try:
        tokens = Lexer(utils.unescape(text, 1), language, inliner.document.settings.syntax_highlight)
    except LexerError, error:
        msg = inliner.reporter.warning(error)
        prb = inliner.problematic(rawtext, rawtext, msg)
        
        return [prb], [msg]

    node = nodes.literal(rawtext, '', classes = classes)

    for classes, value in tokens:
        if classes:
            node += nodes.inline(value, value, classes = classes)
        else:
            node += nodes.Text(value, value)

    return [node], []

code_role.options = {
    'class': directives.class_option,
    'language': directives.unchanged
}

register_canonical_role('code', code_role)


class _CodeBlock(CodeBlock):
    optional_arguments = 1
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
        'number-lines': directives.unchanged
    }
    has_content = True
    
    def run(self):
        self.assert_has_content()
        
        if self.arguments:
            language = self.arguments[0]
        else:
            language = 'text'
        
        set_classes(self.options)
        classes = []
        
        if 'classes' in self.options:
            classes.extend(self.options['classes'])
        
        try:
            tokens = Lexer(u'\n'.join(self.content), language, self.state.document.settings.syntax_highlight)
        except LexerError, error:
            raise self.warning(error)
        
        pre = nodes.literal_block(classes = classes)
        code = nodes.literal(classes = classes)
        code.attributes['data-lang'] = language
        self.add_name(pre)
        self.add_name(code)
        
        for classes, value in tokens:
            if classes:
                code += nodes.inline(value, value, classes = classes)
            else:
                code += nodes.Text(value, value)
        
        pre += code
        
        return [pre]

directives.register_directive('code', _CodeBlock)


class _Translator(HTMLTranslator):
    def set_first_last(self, node):
        pass
    
    def visit_bullet_list(self, node):
        atts = {}
        self.context.append((self.compact_simple, self.compact_p))
        self.compact_p = None
        self.compact_simple = self.is_compactable(node)
        self.body.append(self.starttag(node, 'ul', '', **atts))
    
    def visit_definition(self, node):
        self.body.append('</dt>')
        self.body.append(self.starttag(node, 'dd', ''))
        self.set_first_last(node)

    def depart_definition(self, node):
        self.body.append('</dd>')

    def visit_definition_list(self, node):
        self.body.append(self.starttag(node, 'dl', ''))

    def depart_definition_list(self, node):
        self.body.append('</dl>')
    
    def visit_entry(self, node):
        atts = {}
        
        if isinstance(node.parent.parent, nodes.thead):
            tagname = 'th'
        else:
            tagname = 'td'
        
        node.parent.column += 1
        
        if 'morerows' in node:
            atts['rowspan'] = node['morerows'] + 1
        
        if 'morecols' in node:
            atts['colspan'] = node['morecols'] + 1
            node.parent.column += node['morecols']
        
        self.body.append(self.starttag(node, tagname, '', **atts))
        self.context.append('</%s>' % tagname.lower())
        
        if len(node) == 0:
            self.body.append('&nbsp;')
        
        self.set_first_last(node)
    
    def visit_enumerated_list(self, node):
        atts = {}
        
        if 'start' in node:
            atts['start'] = node['start']
        
        self.context.append((self.compact_simple, self.compact_p))
        self.compact_p = None
        self.compact_simple = self.is_compactable(node)
        self.body.append(self.starttag(node, 'ol', '', **atts))
    
    def visit_list_item(self, node):
        self.body.append(self.starttag(node, 'li', ''))
    
    def depart_list_item(self, node):
        self.body.append('</li>')
    
    def visit_literal(self, node):
        atts = {}
        
        if 'data-lang' in node.attributes:
            atts['data-lang'] = node.attributes['data-lang']
        
        self.body.append(self.starttag(node, 'code', '', **atts))
    
    def visit_literal_block(self, node):
        self.body.append(self.starttag(node, 'pre', ''))
    
    def depart_literal_block(self, node):
        self.body.append('</pre>')
    
    def visit_paragraph(self, node):
        if self.should_be_compact_paragraph(node):
            self.context.append('')
        else:
            self.body.append(self.starttag(node, 'p', ''))
            self.context.append('</p>')
    
    def visit_reference(self, node):
        atts = {}
        
        if 'refuri' in node:
            atts['href'] = node['refuri']
            
            if (self.settings.cloak_email_addresses and atts['href'].startswith('mailto:')):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = True
        else:
            assert 'refid' in node, 'References must have "refuri" or "refid" attribute.'
            
            atts['href'] = '#' + node['refid']
        
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
        
        self.body.append(self.starttag(node, 'a', '', **atts))
    
    def depart_row(self, node):
        self.body.append('</tr>')
    
    def visit_section(self, node):
        self.section_level += 1

    def depart_section(self, node):
        self.section_level -= 1
    
    def visit_table(self, node):
        self.body.append(self.starttag(node, 'table', ''))
    
    def depart_table(self, node):
        self.body.append('</table>')
    
    def visit_tbody(self, node):
        self.body.append(self.starttag(node, 'tbody', ''))
    
    def depart_tbody(self, node):
        self.body.append('</tbody>')
    
    def visit_tgroup(self, node):
        node.stubs = []
    
    def visit_thead(self, node):
        self.body.append(self.starttag(node, 'thead', ''))
    
    def depart_thead(self, node):
        self.body.append('</thead>')
    
    def visit_title(self, node):
        close_tag = '</p>'
        
        if isinstance(node.parent, nodes.topic):
            self.body.append(self.starttag(node, 'p', ''))
        elif isinstance(node.parent, nodes.sidebar):
            self.body.append(self.starttag(node, 'p', ''))
        elif isinstance(node.parent, nodes.Admonition):
            self.body.append(self.starttag(node, 'p', ''))
        elif isinstance(node.parent, nodes.table):
            self.body.append(self.starttag(node, 'caption', ''))
            close_tag = '</caption>'
        elif isinstance(node.parent, nodes.document):
            self.body.append(self.starttag(node, 'h1', ''))
            close_tag = '</h1>'
            self.in_document_title = len(self.body)
        else:
            assert isinstance(node.parent, nodes.section)
            
            h_level = self.section_level + self.initial_header_level - 1
            
            self.body.append(self.starttag(node, 'h%s' % h_level, ''))
            
            atts = {}
            
            if node.hasattr('refid'):
                atts['href'] = '#' + node['refid']
            
            if atts:
                self.body.append(self.starttag({}, 'a', '', **atts))
                close_tag = '</a></h%s>' % (h_level)
            else:
                close_tag = '</h%s>' % (h_level)
        
        self.context.append(close_tag)

class _Writer(Writer):
    def __init__(self):
        Writer.__init__(self)
        
        self.translator_class = _Translator


class Parser(_Parser):
    accepts = (u'.rst',)
    
    
    defaults = {
        'doctitle_xform': 0,
        'input_encoding': 'utf-8',
        'output_encoding': 'utf-8',
        'report_level': 4,
        'smart_quotes': 1,
        'syntax_highlight': 'none'
    }
    
    
    def parse(self, restructuredtext):
        return publish_parts(
            restructuredtext,
            settings_overrides = self.config,
            writer = self._writer
        )['fragment']
    
    def setup(self):
        self.config = deepcopy(self.defaults)
        self.config.update(self.options)
        self.config['file_insertion_enabled'] = 0
        
        self._writer = _Writer()
