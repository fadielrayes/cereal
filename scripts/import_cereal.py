#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import Manufacturer, Cereal

import django
django.setup()

#Cereal.objects.all().delete()

dir_path = os.path.dirname(os.path.abspath(__file__))

cereal_csv = os.path.join(dir_path, 'cereal.csv')

csv_file = open(cereal_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	new_manufacturer, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])
	new_manufacturer.save()

	#print new_cereal
	#print created

	new_cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'])
	
	new_cereal.manufacturer = new_manufacturer
	new_cereal.cereal_type = row['Type']
	new_cereal.calories = row['Calories']
	new_cereal.protein = row['Protein (g)']
	new_cereal.fat = row['Fat'] 
	new_cereal.sodium = row['Sodium']
	new_cereal.dietary_fiber = row['Dietary Fiber']
	new_cereal.carbs = row['Carbs']
	new_cereal.sugars = row['Sugars']
	new_cereal.display_shelf = row['Display Shelf']
	new_cereal.potassium = row['Potassium']
	new_cereal.vit_min = row['Vitamins and Minerals']
	new_cereal.serving_size_weight = row ['Serving Size Weight']
	new_cereal.cups_per_serving = row['Cups per Serving']

	try:
		new_cereal.save()
	except Exception, e:
		print e