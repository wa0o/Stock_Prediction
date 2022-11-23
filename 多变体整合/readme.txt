leea
leea is the fundation of all the leea*

leea_mul_progress
leea_mul_progress uses more process to caculate

leea_elitist
leea_elitist is base on several process. 
it divide species at beign of involve but not in circulate,just like several species.
it uses elitism strategy

leea_inherit
leea_inherit base on leea_elitist,but change the way of inheritance
if parent1's fitness > parent2's fitness, child should inherit parent1 more.
before this, inheritance equation is child'fit = (f1+f2)/2
now it is f' = (f1^2+f2^2)/(f1+f2)
at the same time the probability of child inherit parent1 is f1/(f1+f2)
in this way,i think it may converge to better fitness more quickly

ea
ea is the fundation of all the ea*

ea_dynamic_sample
in most of the, i use a part of sample instead of all sample to reduce caculate.
but i use all sample regularly to correct the deriction of involve.
in this part i use several process just like leea_inherit