# Montessorri Learning
This repo is a blog that helpas anyone who wants to understand what montessorri learning and parenting is all about.
The code is written in django framework, uses Cloudinary for image upload and Xata for its database.

## Prerequisite:
Install Python3

Install Django
```  pip install django   ```

Install Cloudinary
```pip install cloudinary```

For using Cloudinary you need to create a free account( ask me for my credentials for now)
Here's a quick start for Cloudinary using Django framework: https://cloudinary.com/documentation/django_integration

In your django files settings.py replace these with your credentials.
```
cloudinary.config( 
  cloud_name = "YOUR_CLOUD_NAME", 
  api_key = "YOUR_API_KEY", 
  api_secret = "YOUR_API_SECRET" 
)

```

Websites used: 
https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/

https://djangocentral.com/building-a-blog-application-with-django/


Hackmamba Instruction  Manual. https://hackmamba.notion.site/hackmamba/Hackmamba-Content-Hackathon-Participant-Instruction-Manual-7d7e7e25d01246a49260d774daf3da9a
