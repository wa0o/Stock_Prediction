def leea_experiment():
    from data import sample
    from leea import net_params
    from leea import net
    from leea import function
    import numpy as np
    import matplotlib.pyplot as plt
    import limit_evolution_single

    params = limit_evolution_single.p
    print(params.input_size)
    print(params.hidden0)
    print(params.hidden1)
    print(params.species_size)
    print(params.parent_num)
    print(params.ansexual_rate)
    print(params.fitness_decay)
    print(params.num_gen)
    print(params.mutationpower)
    print(params.mutationpowerdecay)
    print(params.mutationrate)
    print(params.mutationratedecay)

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
        print(i+1)
        params.mutationpower *= decayrate
        params.mutationrate *= ratedecayrate
        new_species = net.produce_offspring(species,params.parent_num,params)
        print(i)
        plt.plot(i, abs(species[0].fitness), marker='.', color='black')
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
    plt.pause(2)
    plt.close()
            
            
    for i in range(len(test.test_output)):
        tmp = sample.sample(test.test_input[i],test.test_output[i])
        sample_list.append(tmp)
        
    species.sort(key = function.getfitness,reverse=True)
    x2 = np.arange(0.0, len(sample_list), 1.0)
    z2 = np.arange(0.0, len(sample_list), 1.0)
    z3 = np.arange(0.0, len(sample_list), 1.0)
    
    i = 0
    for sam in sample_list:
        ans = function.node_update(sam,species[0])
        z2[i] = ans
        z3[i] = sam.output
        print('predict:',ans,'fact:',sam.output)
        i += 1

    plt.plot(x2, z2, x2, z3)
    plt.title('LEEA')
    plt.legend(['predict', 'true'])
    plt.xlabel('time')
    plt.ylabel('The Normalized Stock Price')
    plt.show()