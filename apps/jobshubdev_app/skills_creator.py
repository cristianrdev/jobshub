from .models import Language, Framework


def makelanguage():
    all_languages = Language.objects.all()
    all_languages.delete()
    html = Language.objects.create(skill_name = "HTML" , icon_link_language= "devicon-html5-plain colored" )
    css = Language.objects.create(skill_name = "CSS",  icon_link_language= "devicon-css3-plain colored")
    ruby = Language.objects.create(skill_name = "Ruby", icon_link_language= "devicon-ruby-plain colored")
    python = Language.objects.create(skill_name = "Python", icon_link_language= "devicon-python-plain colored")
    
    js = Language.objects.create(skill_name = "Js", icon_link_language= "devicon-javascript-plain colored")
    java = Language.objects.create(skill_name = "JAVASCRIPT", icon_link_language= "devicon-java-plain-wordmark colored")
    csharp = Language.objects.create(skill_name = "C#", icon_link_language= "devicon-csharp-plain colored")
    swift = Language.objects.create(skill_name = "Swift", icon_link_language= "devicon-swift-plain colored")
    go = Language.objects.create(skill_name = "Go", icon_link_language= "devicon-go-plain colored")
    git = Language.objects.create(skill_name = "Git", icon_link_language= "devicon-git-plain colored")
    java = Language.objects.create(skill_name = "Java", icon_link_language= "devicon-java-plain colored")
    php = Language.objects.create(skill_name = "PHP", icon_link_language= "devicon-php-plain colored")
    net = Language.objects.create(skill_name = ".NET", icon_link_language= "devicon-dotnetcore-plain colored")
    postgres = Language.objects.create(skill_name = "Postgresql", icon_link_language= "devicon-postgresql-plain colored")
    sql = Language.objects.create(skill_name = "mysql", icon_link_language= "devicon-mysql-plain colored")



def makeframework():
    all_framekork = Framework.objects.all()
    all_framekork.delete()
    django = Framework.objects.create(skill_name = "Django", icon_link_framework = "devicon-django-plain colored")
    flask = Framework.objects.create(skill_name = "Flask", icon_link_framework = "devicon-flask-original colored")
    rails = Framework.objects.create(skill_name = "Rails", icon_link_framework = "devicon-rails-plain colored")
    spring = Framework.objects.create(skill_name = "Spring", icon_link_framework = "devicon-spring-plain colored")
    react = Framework.objects.create(skill_name = "React", icon_link_framework = "devicon-react-original colored")
    angularjs = Framework.objects.create(skill_name = "Angularjs", icon_link_framework = "devicon-angularjs-plain colored")
    vuejs = Framework.objects.create(skill_name = "vuejs", icon_link_framework = "devicon-vuejs-plain colored")

