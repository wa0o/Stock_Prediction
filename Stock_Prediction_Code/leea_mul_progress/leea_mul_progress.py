def leea_experiment():
    from data import sample
    import numpy as np
    from leea_mul_progress import net_params
    from leea_mul_progress import net
    from leea_mul_progress import function
    import matplotlib
    import matplotlib.pyplot as plt
    import limit_evolution
    from multiprocessing import Pool

    matplotlib.rc("font", family='YouYuan')

    params = limit_evolution.p
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
    print(params.process_num)

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

    x1 = np.arange(0.0, params.num_gen, 1.0)
    y = np.arange(0.0, params.num_gen, 1.0)
    z1 = np.arange(0.0, params.num_gen, 1.0)

    for j in range(params.num_gen):
        # if i%100==0:
        print(j+1)
        params.mutationpower *= decayrate
        params.mutationrate *= ratedecayrate
        species.sort(key=function.getfitness, reverse=True)
        parent_index = function.get_parent_index(species, params.parent_num)
        tmp = []
        test.get_leea_sample(params)
        sample_list = []
        for i in range(len(test.train_output)):
            sample1 = sample.sample(test.train_input[i], test.train_output[i])
            sample_list.append(sample1)
        pool = Pool(processes=params.process_num)
        for i in range(params.process_num):
            one = pool.apply_async(net.produce_offspring, args=(species, params, sample_list, parent_index, i,))
            tmp.append(one)
        pool.close()
        pool.join()
        new_species = []
        for one in tmp:
            new_species.extend(one.get())
        species = new_species.copy()

        temp = 0
        for k in range(len(species)):
            temp += species[k].fitness

        y[j] = temp / len(species)

    y1 = min(y)
    y2 = max(y)
    for i in range(params.num_gen):
        if y2 != y1:
            z1[i] = (y[i] - y1) / (y2 - y1)

    # plt.plot(x1, z1)
    # plt.title('LEEA-fitness')
    # plt.xlabel('generation')
    # plt.ylabel('fitness')
    # plt.show()
            
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
    plt.title('LEEA(mul_progress)')
    plt.legend(['predict', 'true'])
    plt.xlabel('time')
    plt.ylabel('The Normalized Stock Price')
    plt.show()
        