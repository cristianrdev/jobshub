from .models import Language, Framework


def makelanguage():
    all_languages = Language.objects.all()
    all_languages.delete()
    html = Language.objects.create(skill_name = "HTML" , icon_link_language= "devicon-html5-plain colored" )
    css = Language.objects.create(skill_name = "CSS",  icon_link_language= "devicon-css3-plain colored")
    ruby = Language.objects.create(skill_name = "RUBY", icon_link_language= "devicon-ruby-plain colored")
    python = Language.objects.create(skill_name = "PYTHON", icon_link_language= "devicon-python-plain colored")
    sql = Language.objects.create(skill_name = "SQL", icon_link_language= "devicon-mysql-plain colored")
    js = Language.objects.create(skill_name = "JS", icon_link_language= "devicon-javascript-plain colored")
    java = Language.objects.create(skill_name = "JAVA", icon_link_language= "devicon-java-plain-wordmark colored")
    csharp = Language.objects.create(skill_name = "C#", icon_link_language= "devicon-csharp-plain colored")
    go = Language.objects.create(skill_name = "GO", icon_link_language= "devicon-go-plain colored")



def makeframework():
    all_framekork = Framework.objects.all()
    all_framekork.delete()
    django = Framework.objects.create(skill_name = "Django", icon_link_framework = "devicon-django-plain colored")
    flask = Framework.objects.create(skill_name = "Flask", icon_link_framework = "devicon-flask-original colored")
    rails = Framework.objects.create(skill_name = "Rails", icon_link_framework = "devicon-rails-plain colored")
    spring = Framework.objects.create(skill_name = "Spring", icon_link_framework = "devicon-spring-plain colored")

# def makeposition():
#     all_state_positions = StatePosition.objects.all()
#     all_state_positions.delete()
#     open_position = StatePosition.objects.create(state_name = "Proceso iniciado, en contratación")
#     evaluating = StatePosition.objects.create(state_name = "Evaluando candidatos")
#     closed = StatePosition.objects.create(state_name = "Proceso cerrado")
