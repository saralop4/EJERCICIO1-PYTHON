presion_sistolica = int(input())
presion_diastolica = int(input())

if presion_sistolica<91 and presion_diastolica<63: 
                                            print("hipotension","","alerta amarilla")
elif presion_sistolica>=91 and presion_sistolica<=133  and presion_diastolica>=63 and presion_diastolica<=76: 
                                                                        print("ideal","","alerta verde") 
elif presion_sistolica>=134 and presion_sistolica<=161  and presion_diastolica>=77 and presion_diastolica<=104: 
                                                                        print("normal","","alerta verde")   
elif presion_sistolica>=162 and presion_sistolica<=187  and presion_diastolica>=105 and presion_diastolica<=118: 
                                                                        print("normal-alta","","alerta amarilla")
elif presion_sistolica>=188 and presion_sistolica<=200  and presion_diastolica>=119 and  presion_diastolica<=125: 
                                                                        print("hta grado 1","","alerta roja") 
elif presion_sistolica>=201 and presion_sistolica<=213  and presion_diastolica>=126 and presion_diastolica<=145: 
                                                                        print("hta grado 2","","alerta roja")                                                                                                                          
elif presion_sistolica>=214  and presion_diastolica>=146:      
                                                     print("hta grado 3","","alerta roja")  
elif presion_sistolica>=152  and presion_diastolica<79:      
                                                     print("hipertension solo sistolica","","alerta naranja")
else:
    print('no se puede determinar la categoria',"","alerta gris")     






                                                                                                                     



                                    