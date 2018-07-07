## Info:

Das hier ist mein locales Setup. Vor dem starten musst du dir einen Dump der Database ziehen und die `settings.py` entsprechend anpassen.

Ich habe außerdem alle hochgeladenen Media files ausgelassen. Diese musst du dir ebenfalls vom Server ziehen oder einen Symlink anlegen.



##**Dependencies:**

```bash
> pip freeze
BeautifulSoup==3.2.1
beautifulsoup4==4.2.1
cmsplugin-contact==1.0.0
cmsplugin-filer==0.9.5
cmsplugin-filery==1.0.1
cmsplugin-vimeo==0.1
cmsplugin-youtube==0.1.5a1
cmsplugin-zinnia==0.4
Django==1.5.1
django-appconf==1.0.2
-e git://github.com/Fantomas42/django-blog-zinnia.git@cffdd71b8ffff76f238e64b01ec873b6a5b98a89#egg=django_blog_zinnia
django-classy-tags==0.4
django-cms==2.4.2
django-cms-simple-events==0.4.1
django-filer==0.9.5
django-hvad==0.3
django-imagekit==3.2.6
django-mathfilters==0.1.3
django-missing==0.1.11
django-mptt==0.5.2
django-polymorphic==0.5.1
django-sekizai==0.7
django-shop==0.2.0
django-shop-categories==0.8b2
django-shop-simplenotifications==0.1.3
django-tagging==0.3.1
django-tinymce==1.5.1
django-treeadmin==0.4
django-xmlrpc==0.1.5
djangocms-utils==0.9.5
easy-thumbnails==2.4.2
flup==1.0.3.dev20110405
html5lib==1.0b1
jsonfield==0.9.17
MySQL-python==1.2.4
pilkit==1.1.12
Pillow==2.7.0
pyparsing==1.5.7
pytz==2013b0
six==1.3.0
South==0.8.1
```



## Run:

``` > python mangage.py runserver``` 



##Django Apps:

**auszeichnungen:**

Speichert Veranstalter und gewonene Preise. Diese Preise können Weinen zugeordnet werden und tauchen dann auf der Weindetailseite auf. Die Seite "Auszeichnungen" auf der Website ist jedoch manuell geführt. Ich hatte bereits angefangen ein Plugin zu schreiben um die Auszeichnungen automatisch zu listen aber Toska hatte ihre Liste schon manuell erstellt und war zufrieden damit.



**boehme_toechter:**

Die Grundwebsite basierend auf django-cms.



**glossar:**

Speichert Fachbegriffe aus dem Weinanbau. Diese konnte man dann in Texten verlinken und erzeugte dann eine info bubble beim Hovern. Wurde nie richtig angenommen oder benutzt. Scheint also unwichtig zu sein.



**myadressmodel:**

Ein deutsches Adressmodel, dass für den Shop verwendet wird.



**simple_events:**

Simple kleine events die auf der Website under Aktuelles ganz rechts als Termine auftauchen.



**webshop:**

Der Webshop basierend auf django-shop. Hier findest du alle templates und modelle für den Shop.

