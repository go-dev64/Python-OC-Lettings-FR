Deployment
===============

This section defines a differents ways of deploying the application.
We assume that the application is already installed (see get started).

Local
-----

To launch the Oc_lettings_site loacaly, type in your console:

.. code-block:: console

   (.venv) $ python manage.py runserver


The console will display:

.. code-block:: console

   Performing system checks...
   System check identified no issues (0 silenced).
   October 19, 2023 - 15:45:15
   Django version 3.0, using settings 'oc_lettings_site.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.


In your browser, enter **localhost:8000** or click on link inside a console.
You are on Oc_lettings_site home page .

  
Pull docker Image
-----------------
Docker is a platform for launching applications using software containers.
We assume that docker is installed on you machine and hate to a docker hub account.

Docker : `Téléchargement de Docker <https://www.docker.com/get-started>`_.


In docker HUB, selected the lastest image Tags of Repository : `Repository Oc_lettings <https://hub.docker.com/r/godev64/oc_lettings/tags>`_ and copy the command to pull this one.
 
Paste the command on your terminal, like that.

.. code-block:: console

   (.venv) $ docker pull godev64/oc_lettings:latest

Check any local server  is running and Run docker like that:

.. code-block:: console

   (.venv) $ docker compose up

In your browser, enter **localhost:8000** or click on link inside a console.
You are on Oc_lettings_site home page .

and stop Docker with:

.. code-block:: console

   (.venv) $ docker compose down



Render deployment
------------------

A CI/CD pipeline has been set up for the development and deployment of this application. It is monitored on the CircleCI platform.
When a commit is pushed on master branch of repository GITHUB, a workflow is launched with compliation and testing procress.
then if test is passed, workflow build and push an docker image of new version on docker hub repository.
To finish , it deploy on Render.

**Requirements**:

    - GITHUB account
    - Docker hub account(username and password)
    - Circle CI account 
    - Render account , website project with deploy hook url.


Render configuration
--------------------

In environment settings of Render, you have to define environment variable of:
.. code-block:: console

    SECRET_KEY_DJANGO= secret key of django
    SENTRY_DNS=dns of sentry


Circle Ci configuration 
-----------------------

In your account Cercle Ci , create a new project from repository GITHUB of apllication OC_lettings.
Then  in **Project settings**, select **Environment Variables**, and create 5 new variables like that:

.. code-block:: console

    DOCKERHUB_PASSWORD=your docker hub password
    DOCKERHUB_USERNAME=your docker hub username 
    RENDER_KEY=your deploy hook url of  render
    SECRET_KEY_DJANGO= secret key of django
    SENTRY_DNS=dns of sentry

Now, a simple push on your master branch github, launch workflow Cercle Ci and deployment on render.
You can see result on your render url.




 









