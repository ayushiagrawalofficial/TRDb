from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from resources.models import StudyResource, Technology, Vote

admin.site.register(StudyResource, GuardedModelAdmin)
admin.site.register(Technology, GuardedModelAdmin)
admin.site.register(Vote, GuardedModelAdmin)
