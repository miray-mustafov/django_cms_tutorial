# Django CMS Tutorial

![project_logo.png](photos/project_logo.png)

## Table of Contents

* [Setup](#setup)
* [Folder Structure](#folder-structure)
* [Theory](#theory)
* [Useful Commands](#useful-commands)
* [Screenshots](#screenshots)

## Setup

```bash
uv sync
```

```bash
django-admin startproject myproject --template https://github.com/django-cms/cms-template/archive/5.1.tar.gz
```

Delete useless files like the initialized requirements.txt, etc.

```bash
uv run src/manage.py migrate
```

```bash
uv run src/manage.py createsuperuser
```

```bash
uv run src/manage.py cms check
```

```bash
uv run src/manage.py runserver 8000
```

## Useful Commands

```bash
uv run src/manage.py startapp pages
```

```bash
uv run python -m directory_tree -I .venv node_modules __pycache__ data media static out temporary
```

```bash
cms list plugins
cms delete-orphaned-plugins
```

## Folder Structure

todo

## Theory

### CMS (Content Management System)

- Why: Non-technical users to manage content in a website.
- Examples: **Djnago CMS**, Strapi (JS Headless CMS), Wordpress (PHP traditional CMS)
- What:   
  a system for creating, editing, organizing, and publishing website content through a user interface  
  usually provides pages, content blocks, media management, workflows, permissions, and previews

### CMS Page:

- Why:  
  To give editors an entity that can be managed visually instead of being hardcoded  
  It is the basic container where CMS content, **placeholders**, aliases, **plugins**, and **apphooks** can live.    
<br>
- Examples:  
  home page, about page, contact page, polls page, blog page, product landing page  
<br>
- What:  
  a page object managed by django CMS   
  usually has a title, slug, language versions, template, and placeholders  
  can contain plugins and static content blocks  
  can also have advanced settings, such as an attached apphook  
  can be nested into a page tree, so the site structure is editable by content editors    
<br>
- How it works:  
  An editor creates a page in the CMS admin or toolbar  
  selects a template for it  
  adds content into placeholders  
  optionally attaches plugins or apphooks  
  django CMS then serves that page at its URL  
<br>
- **So a CMS Page is more like**:  
  "this is an editable page in the site structure"  
  not:  
  "a hardcoded Django view template only"  

### Plugin

- Why: same as CMS  
<br>
- Examples: poll widget, image gallery, form, card, banner, product teaser  
<br>
- What:  
  drag&drop, reusable, editable page fragments/content which will be managed by the editors  
<br>
- Consists of:
    - Plugin model [models.py](src/myproject/contrib/cms_polls/models.py)   
      stores data for a content block
      inherits from `CMSPlugin`
    - Plugin publisher [cms_plugins.py](src/myproject/contrib/cms_polls/cms_plugins.py)    
      tells the CMS how to render the content block  
      defines: name, plugin model  
      which template to use  
      how to prepare the context for the template  
      inherits from `CMSPluginBase`  
<br>
- How it works:  
  When an editor clicks + in a placeholder:
  django CMS shows the list of registered plugins
  editor selects one
  django CMS creates a plugin instance in the database
  the plugin data is saved
  the chosen template renders it on the page


- **So a plugin is more like**:  
  "drop this widget here"  
  not:  
  "serve this app at this URL"

### Apphook
[cms_apps.py](src/myproject/contrib/polls_cms_integration/cms_apps.py)  
there is screenshot below too
- Why:  
  To attach a whole Django app to a CMS page, so the app becomes part of the CMS site structure instead of being
  hardcoded in the project URLs.  
  Useful when you want editors to choose which CMS page should act as the entry point for an app.
- Examples: polls app, blog app, shop/catalog app, forum section
- **What**:    
  [app][hook] - hook/mount an app to a CMS page  
  a CMS integration mechanism  
  it is defined with a `CMSApp` subclass and registered in the apphook pool  
  it provides URL patterns for that app  
  it lets django CMS delegate part of the URL space to that application
- How it works:  
  Django CMS looks at the page’s advanced settings  
  editor selects an apphook for that page  
  CMS mounts the app’s URL patterns under that page  
  requests below that page are routed to the attached Django app
- **So an apphook is more like**:  
  "mount this app under this CMS page"  
  not:  
  "drop this widget into the page content"

### models.py

- Place to define plugin models. How plugins will be stored in the database.

### cms_plugins.py

- Place to define plugin publishers. How plugins will be rendered on the page.

## Screenshots

- Polls
  ![poll_choices.png](photos/poll_choices.png)
  ![poll_results.png](photos/poll_results.png)


- Applied apphook to polls
  ![polls_applied_apphook.png](photos/polls_applied_apphook.png)
