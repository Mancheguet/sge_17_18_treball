# -*- coding: utf-8 -*-

from odoo import models, fields, api

class varietysnail(models.Model):
    _name = 'fastsnail.varietysnail'

    name = fields.Char()
    idvariety = fields.Integer()
    thermalresist = fields.Char()
    description = fields.Text()
    totalsnails = fields.One2many('fastsnail.snail','snailclass')#fields.Integer() #total de caracoles que tienen este timpo , tendrá que ser computada  y se dará en kg


class snail(models.Model):
    _name = 'fastsnail.snail'

    name = fields.Char()
    idsnail = fields.Integer()
    snailclass = fields.Many2one('fastsnail.varietysnail')#fields.Char() #tendrá que darte a elegir entre las classe creada anteriomente (la parte de arriba)
    description = fields.Text()
    photo = fields.Binary() # foto del caracol

class competition(models.Model):
    _name = 'fastsnail.competition'

    name = fields.Char()
    idcompetition = fields.Integer()
    startdate = fields.Datetime() #data en la que empieza la temporada 
    enddate = fields.Datetime() #data en la que termina la temporada
    totalSeasons = fields.Integer()

class season(models.Model):
    _name = 'fastsnail.season'

    name = fields.Char()
    idseason = fields.Integer()
    startdate = fields.Datetime() #data en la que empieza la temporada 
    enddate = fields.Datetime() #data en la que termina la temporada
    description = fields.Text()
    totalrace = fields.Text() #total de carreras con lista , computada de las carreras que esten en esta season
    totalsnails = fields.Integer() #total de caracoles participan en la temporada computado usando la lista de las carreras

class race(models.Model):
    _name = 'fastsnail.race'

    name = fields.Char()
    idrace = fields.Integer()
    startdate = fields.Datetime() #data en la que empieza la temporada 
    description = fields.Text()
    totalsnails = fields.Integer() #total de caracoles participan en la temporada computado usando la lista de las carreras    

class classification(models.Model):
	_name = 'fastsnail.classification'

	name = fields.Char()
	idclassification = fields.Integer()
	idrace = fields.Integer() # relación entre la carrera y la classificación ( tendrá que dar a elegir que carrera queremos)
	idfirstsnail = fields.Integer() # id del caracol que ha qedado primero
	idsecondsnail = fields.Integer() # id del caracol que ha qedado segunod
	idthirdsnail = fields.Integer() # id del caracol que ha qedado tercero


class employee(models.Model):
	_name = 'fastsnail.employee'

  	idemployee = fields.Integer()
	name = fields.Char()
	surname = fields.Char()
	phone = fields.Integer()

#CREAR UNA TAULA INTERMIG -> CARERRA-CARAGOL-POSICIÓ 





