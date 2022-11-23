def leea_experiment():
    from data import sample
    from leea_mul_progress import net_params
    from leea_mul_progress import net
    from leea_mul_progress import function
    import numpy as np
    import matplotlib.pyplot as plt
    from multiprocessing import Pool


    params = net_params.net_params()

    test = sample.test_sample()
    test.get_leea_sample(params)
    sample_list = []
    for i in range(len(test.train_output)):
        tmp = sample.sample(test.train_input[i],test.train_output[i])
        sample_list.append(tmp)

    decayrate = pow((1-params.mutationpowerdecay),1/params.num_gen)
    ratedecayrate = pow((1-params.mutationratedecay),1/params.num_gen)

    species = net.create_first_generation(params)

    for i in range(len(species)):
        species[i].fitness = function.evaluate(species[i],sample_list)
    for i in range(params.num_gen):
        # if i%100==0:
        print(i)
        params.mutationpower *= decayrate
        params.mutationrate *= ratedecayrate
        species.sort(key = function.getfitness,reverse=True)
        parent_index = function.get_parent_index(species,params.parent_num)
        tmp = []
        test.get_leea_sample(params)
        sample_list = []
        for j in range(len(test.train_output)):
            sample1 = sample.sample(test.train_input[j],test.train_output[j])
            sample_list.append(sample1)
        pool = Pool(processes=params.process_num)
        for j in range(params.process_num):
            one = pool.apply_async(net.produce_offspring,args=(species,params,sample_list,parent_index,j,))
            tmp.append(one)
        pool.close()
        pool.join
        new_species = []
        for one in tmp:
            new_species.extend(one.get())
        species = new_species.copy()
            
    species.sort(key = function.getfitness,reverse=True)

    sample_list =[]      
    test.get_test_sample(params)
    for i in range(len(test.test_output)):
        tmp = sample.sample(test.test_input[i],test.test_output[i])
        sample_list.append(tmp)
        
    species.sort(key = function.getfitness,reverse=True)
    for sam in sample_list:
        ans = function.node_update(sam,species[0])
        print('predict:',ans,'fact:',sam.output)