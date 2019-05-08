RaDop Dashboard
===============

Centro de Inteligência do RaDop

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: GPLv3

O dashboard é um software que dá apoio ao RaDop.


Comandos Básicos
----------------

Para buildar o projeto:

::

  docker-compose -f local.yml up --build

Para remover o projeto:

:: 

  docker-compose -f local.yml down --rm all -v

Configurando o usuário
^^^^^^^^^^^^^^^^^^^^^^

* Para criar uma **conta normal de usuário**, basta ir até Inscreva-se e preencher o formulário. Depois de enviá-lo, você verá uma página "Verificar seu endereço de e-mail".
Vá para o seu console para ver uma mensagem de verificação de e-mail simulada. Copiei o link no seu navegador e pronto.

* Para criar um **superuser account**, use esse comando::

    $ python manage.py createsuperuser

Verificação de Tipo
^^^^^^^^^^^^^^^^^^^

Verificações de tipo em execução com mypy:

::

  $ mypy dashboard

Cobertura de Teste
^^^^^^^^^^^^^^^^^^

Para executar os testes, verifique sua cobertura de teste e gere um relatório de cobertura de HTML::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Executando testes com py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Recarregamento ao vivo e compilação CSS Sass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Movido para `Live reloading e SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





