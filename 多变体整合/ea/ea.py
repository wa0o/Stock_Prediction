def ea_experiment(): 
    from data import sample
    from ea import net_params
    from ea import net
    from ea import function
    import numpy as np
    import matplotlib.pyplot as plt
    from multiprocessing import Pool
    
    params = net_params.net_params()
    test = sample.test_sample()
    test.get_ea_sample(params)

    sample_list = []
    for i in range(len(test.train_output)):
        tmp = sample.sample(test.train_input[i],test.train_output[i])
        sample_list.append(tmp)

    decayrate = pow((1-params.mutationpowerdecay),1/params.num_gen)
    ratedecayrate = pow((1-params.mutationratedecay),1/params.num_gen)

    species = net.create_first_generation(params)

    function.pro_evaluate_all(species,sample_list,params)#change here
        
    for i in range(params.num_gen):#change process run
        print(i)
        params.mutationpower *= decayrate
        params.mutationrate *= ratedecayrate
        species.sort(key = function.getfitness,reverse=True)
        parent_index = function.get_parent_index(species,params.parent_num)
        tmp = []
        new_species = []
        pool = Pool(processes=params.process_num)
        for j in range(params.process_num):
            one = pool.apply_async(net.produce_offspring,args=(species,params,sample_list,parent_index,j,))
            tmp.append(one)
        pool.close()
        pool.join
        for one in tmp:
            new_species.extend(one.get())
        species = function.get_next_generation(species,new_species,params.species_size)
            
    species.sort(key = function.getfitness)

    test.get_test_sample(params)
    sample_list = []
    for i in range(len(test.test_output)):
        tmp = sample.sample(test.test_input[i],test.test_output[i])
        sample_list.append(tmp)
    
    for sam in sample_list:
        ans = function.node_update(sam,species[0])
        print('predict:',ans,'fact:',sam.output)