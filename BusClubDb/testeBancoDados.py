# -*- coding: utf-8 -*-
import BusStopClubServer

horarios = BusStopClubServer.BusStopClubServer.get_horario('UFSM', 'Universidade', 'FV', 'Util')

#for hora in horarios:
    #print hora

#print 'Ha',horarios.__len__(),'horarios disponiveis.'

BusStopClubServer.BusStopClubServer.setPos('UFSM', 'Bombeiros', 'FV', 'Util', 0, 0, '6:10')
