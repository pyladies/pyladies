---
layout: default
title: Fale Conosco
permalink: /contact/
icon: icon-envelope
tab: true
order: 4
---
<div class="contact">
	<div class="row" style="padding-left: 50px;">
	  <div class="12u">
	    <form method="post" action="formulario.php">
        <div>
          <div class="row half">
            <div class="6u">
	            <input type="text" name="nome" id="name" placeholder="Name" />
            </div>
            <div class="5u">
              <input type="text" name="email" id="email" placeholder="Email" />
            </div>
          </div>
          <div class="row half">
            <div class="11u">
              <input type="text" name="assunto" id="assunto" placeholder="Assunto" />
            </div>
          </div>
          <div class="row half">
            <div class="11u">
					    <textarea name="mensagem" id="mensagem" placeholder="Mensagem"></textarea>
            </div>
          </div>
          <div class="row but">
            <div class="11u">
               <input name="enviar" type="submit" value="Enviar" class="button form-button-submit"/>
               <input name="enviar" type="reset" value="Limpar" class="button form-button-reset" />
            </div>
          </div>
        </div>
      </form>
	  </div>
	</div>
</div>