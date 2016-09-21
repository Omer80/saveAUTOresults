#include "auto_f2c.h"
#include <math.h>

#define F2C -1

/* ---------------------------------------------------------------------- */
/*          Model Equations                                               */
/* ---------------------------------------------------------------------- */
int func (integer ndim, const doublereal *u, const integer *icp,
          const doublereal *par, integer ijac,
          doublereal *f, doublereal *dfdu, doublereal *dfdp)
{
  /* System generated locals */
  /* Local variables */
  doublereal U1,U2,U3,U4;
  doublereal a,b;
  doublereal pi, num_periods,L;
  pi = atan(1.) * 4.0;  
  
  /* Defining the parameters */
 
  a=par[1+F2C];
  b=par[2+F2C];
  
  /* Function Body */
  U1 = u[0];
  U2 = u[1];
  U3 = u[2];
  U4 = u[3];
  
  /* Loading into internal system of equations */
  
  f[0] = eq1;
  f[1] = eq2;
  f[2] = eq3;
  f[3] = eq4;

  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int stpnt (integer ndim, doublereal x,
           doublereal *u, doublereal *par)
{
  /* local variables */
  doublereal U1,U2,U3,U4;
  doublereal a,b;
  doublereal pi, num_periods,L;
  /*  defining the numerical value of the parameters */

  a  = 25;
  b  = 1.2;
  
  /* Loading into internal parameters array */

  par[1+F2C] = a;
  par[2+F2C] = b;
  
  U1 = 0;
  U2 = 0;
  U3 = 0;
  U4 = 0;
  
  /* Loading into internal variable array */
 
  u[0] = U1;  
  u[1] = U2;  
  u[2] = U3;  
  u[3] = U4;  

  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int pvls (integer ndim, const doublereal *u,
          doublereal *par)
{

  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int bcnd (integer ndim, const doublereal *par, const integer *icp,
          integer nbc, const doublereal *u0, const doublereal *u1, integer ijac,
          doublereal *fb, doublereal *dbc)
{  
  
  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int icnd (integer ndim, const doublereal *par, const integer *icp,
          integer nint, const doublereal *u, const doublereal *uold,
          const doublereal *udot, const doublereal *upold, integer ijac,
          doublereal *fi, doublereal *dint)
{
    return 0;
}

/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int fopt (integer ndim, const doublereal *u, const integer *icp,
          const doublereal *par, integer ijac,
          doublereal *fs, doublereal *dfdu, doublereal *dfdp)
{
    return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */

