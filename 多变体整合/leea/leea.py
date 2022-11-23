def leea_experiment():
    from data import sample
    from leea import net_params
    from leea import net
    from leea import function
    import numpy as np
    import matplotlib.pyplot as plt


    params = net_params.net_params()

    test = sample.test_sample()
    test.get_leea_sample(params)
    test.get_test_sample(params)

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
        new_species = net.produce_offspring(species,params.parent_num,params)
        plt.plot(i,species[0].fitness,marker = '.',color='coral')
        plt.ylabel('fitness')
        plt.draw()
        plt.pause(0.01)
        species = new_species
        sample_list = []
        test.get_leea_sample(params)
        for k in range(len(test.train_output)):
            tmp = sample.sample(test.train_input[k],test.train_output[k])
            sample_list.append(tmp)
        for j in range(len(species)):
            fit = function.evaluate(species[j],sample_list)
            species[j].fitness *= (1-params.fitness_decay)
            species[j].fitness += fit
        
            
            
    for i in range(len(test.test_output)):
        tmp = sample.sample(test.test_input[i],test.test_output[i])
        sample_list.append(tmp)
        
    species.sort(key = function.getfitness,reverse=True)
    
    for sam in sample_list:
        ans = function.node_update(sam,species[0])
        print('predict:',ans,'fact:',sam.output)