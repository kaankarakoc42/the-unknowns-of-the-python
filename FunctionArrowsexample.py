def kinetic_energy(m:'in KG'=10, v:'in M/S'=5)->'Joules': 
  return 1/2*m*v**2



def happy_level(c:int=1,p:int=70)->...:
    return c*p


print(kinetic_energy.__annotations__,"\n",happy_level.__annotations__)

"""
its only for declaration functions after the arrow (->) its saying basically what you are returning 
and we using colon(:) sign for explanation that why we gives arguman
"""