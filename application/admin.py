from django.contrib import admin
from application.models import JobOpenings, Questionnaire, Rsa

# class ChoicesInline(admin.StackedInline):
    # model = Choices
    # extra = 2
	
	
	
# class SelectiveQuestionsAdmin(admin.ModelAdmin):
	# fieldsets = [
		 # ('Job Title',       {'fields': ['job_opening']}),
        # (None,               {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date']}),
    # ]
	# inlines = [ChoicesInline]



# Register your models here.
admin.site.register(JobOpenings)
admin.site.register(Questionnaire)
admin.site.register(Rsa)



