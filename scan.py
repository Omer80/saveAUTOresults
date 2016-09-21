# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:45:37 2016

@author: Omer Tzuk <omertz@post.bgu.ac.il>
"""
#=================
# AUTO scan file
#=================
from auto import *

def scanBif(modelname,NMX=5000,NPR=50000,DSMAX=0.025,DS=0.000113,IPLT=0):
	tf = run(e=modelname,c=modelname,NMX=NMX,NPR=NPR,DSMAX=DSMAX,IPS=1,ISP=2,DS=DS,IPLT=IPLT)
	tb = run(e=modelname,c=modelname,NMX=NMX,NPR=NPR,DSMAX=DSMAX,IPS=1,ISP=2,DS=-DS,IPLT=IPLT)
	bif = merge(tf+tb)
	bif = rl(bif)
	print "Number of Hopf bifurcations: ",len(bif('HB'))
	return bif

def scanHB(modelname,initial_state,HB=1,NMX=5000,NPR=1000,DSMAX=0.0025,DS=0.00001,UZR={'a':[0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]}):
	if type(initial_state)!=str:
		thb = run(bif('HB'+str(HB)),ISP=1,IPS=2,NMX=NMX,NPR=NPR,DSMAX=DSMAX,DS=DS,ICP=['a',11],UZR=UZR)
	else:
		thb_f = run(e=modelname,c=modelname,dat=initial_state,ISP=1,IPS=2,NMX=NMX,NPR=NPR,DSMAX=DSMAX,DS=DS,ICP=['a',11],UZR=UZR)
		thb_b = run(e=modelname,c=modelname,dat=initial_state,ISP=1,IPS=2,NMX=NMX,NPR=NPR,DSMAX=DSMAX,DS=-DS,ICP=['a',11],UZR=UZR)
		thb=merge(thb_f+thb_b)
		thb=rl(thb)
	return thb

def scanONL(HB,UZ=1,ICP=[11],UZR={11:[10,20,30,40,50,100]},NPR=5,DSMAX=0.001,DS=0.00001,RL1=100):
	onl = run(thb('UZ'+str(UZ)),ICP=ICP,UZR=UZR,NPR=NPR,DSMAX=DSMAX,RL1=RL1)
	return onl
	
def saveBif(bifurcation,cont_parm='a',fname="bif_data"):
	import deepdish as dd
	continuation=[]
	for i,branch in enumerate(bifurcation):
		print "Branch",i+1, " of shape ", branch.toarray().shape
		LABs = []
		TYs = []
		for solution in branch:
			LABs.append(solution['LAB'])
			TYs.append(solution['TY name'])
		data = branch.toarray()
		branch_dict={'LAB':LABs,'TY':TYs,str(cont_parm):data[0],'L2norm':data[1],
		              'U1':data[2],'U2':data[3],'U3':data[4],'U4':data[5],
		              'sol':False}
		continuation.append(branch_dict)
	dd.io.save(fname+'.hdf5', continuation)

def saveTuring(hb,cont_parm='a',fname="solution_data"):
	import numpy as np
	import deepdish as dd
	turing = hb()
	c=[]
	t=[]
	U1sol=[]
	U2sol=[]
	U3sol=[]
	U4sol=[]
	U1=[]
	U2=[]
	U3=[]
	U4=[]
	nx = []
	lx = []
	for solution in turing:
		c.append(solution[cont_parm])
		t.append(solution['t'])
		nx.append(len(solution['t']))
		lx.append(solution['PAR(11)'])
		U1sol.append(solution['U1'])
		U2sol.append(solution['U2'])
		U3sol.append(solution['U3'])
		U4sol.append(solution['U4'])
		U1.append(np.mean(solution['U1']))
		U2.append(np.mean(solution['U2']))
		U3.append(np.mean(solution['U3']))
		U4.append(np.mean(solution['U4']))
	c = np.array(c)
	t  = np.array(t)
	nx = np.array(nx)
	lx = np.array(lx)
	U1sol=np.array(U1sol)
	U2sol=np.array(U2sol)
	U3sol=np.array(U3sol)
	U4sol=np.array(U4sol)
	U1=np.array(U1)
	U2=np.array(U2)
	U3=np.array(U3)
	U4=np.array(U4)
	solution = {'sol':True,str(cont_parm):c,'t':t,
	            'U1sol':b1sol,'U2sol':b2sol,'U3sol':s1sol,'U4sol':s2sol,
	            'U1':b1,'U2':b2,'U3':s1,'U4':s2,
	            'lx':lx,'nx':nx,'nd':1}
	dd.io.save(fname+'.hdf5', [solution])
