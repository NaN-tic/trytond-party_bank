======
Bancos
======

Módulo que le permite la gestión de bancos y datos bancarios de empresas y
terceros en su ERP

Menú
====

|menu_bank_view|

.. |menu_bank_view| tryref:: res.menu_bank_view/complete_name

Cada banco dispone de:

* Código
* BIC/Swift

Empresa y Terceros
==================

En la ficha de empresa o de terceros puede añadir cuentas bancarias. Cada
cuenta bancaria está relacionada con:

* Banco
* Número de cuenta bancaria
* Número de cuenta IBAN
* Moneda
* Código nacional
* BIC/Swift

Caso que tuviera más de una cuenta bancaria en la empresa, puede marcar una
como cuenta por defecto.

Módulos que dependen
====================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /party/index

Dependencias
------------

* Terceros_

.. _Terceros: ../party/index.html
