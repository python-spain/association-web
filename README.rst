Python-Spain Backoffice/Admin application
=========================================

Setup initial development environment
-------------------------------------

.. code-block:: console

    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manage.py loaddata initial_user


NOTE: requires python3.3




`initial_user` fixture inserts a test supeuser
with 'admin@admin.com' as username and '123123'
as password.


