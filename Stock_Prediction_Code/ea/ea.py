def ea_experiment(): 
    from unittest import result
    from data import sample
    import numpy as np
    from ea import net_params
    from ea import net
    from ea import function
    import time
    from multiprocessing import Pool
    import matplotlib
    import matplotlib.pyplot as plt
    import evolution

    matplotlib.rc("font", family='YouYuan')

    params = evolution.p
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
    test.get_ea_sample(params)
    test.get_test_sample(params)

    sample_list = []
    for i in range(len(test.train_output)):
        tmp = sample.sample(test.train_input[i],test.train_output[i])
        sample_list.append(tmp)

    decayrate = pow((1-params.mutationpowerdecay),1/params.num_gen)
    ratedecayrate = pow((1-params.mutationratedecay),1/params.num_gen)

    species = net.create_first_generation(params)

    function.pro_evaluate_all(species, sample_list, params)

    x1 = np.arange(0.0, params.num_gen, 1.0)
    y = np.arange(0.0, params.num_gen, 1.0)
    z1 = np.arange(0.0, params.num_gen, 1.0)

    for i in range(params.num_gen):
        print(i)
        params.mutationpower *= decayrate
        params.mutationrate *= ratedecayrate
        species.sort(key=function.getfitness, reverse=True)
        plt.plot(i, abs(species[0].fitness), marker='.', color='black')
        plt.ylabel('fitness')
        plt.draw()
        plt.pause(0.01)
        parent_index = function.get_parent_index(species, params.parent_num)
        tmp = []
        new_species = []
        pool = Pool(processes=params.process_num)
        for j in range(params.process_num):
            one = pool.apply_async(net.produce_offspring, args=(species, params, sample_list, parent_index, j,))
            tmp.append(one)
        pool.close()
        pool.join
        for one in tmp:
            new_species.extend(one.get())
        species = function.get_next_generation(species, new_species, params.species_size)

        temp = 0
        for j in range(len(species)):
            temp += species[j].fitness
        y[i] = temp / len(species)
    plt.pause(2)
    plt.close()

    y1 = min(y)
    y2 = max(y)
    for i in range(params.num_gen):
        if y2 != y1:
            z1[i] = (y[i] - y1) / (y2 - y1)

    # plt.plot(x1, z1)
    # plt.title('EA-fitness')
    # plt.xlabel('generation')
    # plt.ylabel('fitness')
    # plt.show()
            
    for i in range(len(test.test_output)):
        tmp = sample.sample(test.test_input[i],test.test_output[i])
        sample_list.append(tmp)

    x2 = np.arange(0.0, len(sample_list), 1.0)
    z2 = np.arange(0.0, len(sample_list), 1.0)
    z3 = np.arange(0.0, len(sample_list), 1.0)

    i = 0
    for sam in sample_list:
        ans = function.node_update(sam,species[0])
        z2[i] = ans
        z3[i] = sam.output
        print('predict:',ans,'fact:',sam.output)
        species.sort(key = function.getfitness)
        i += 1

    plt.plot(x2, z2, x2, z3)
    plt.title('EA')
    plt.legend(['predict', 'true'])
    plt.xlabel('time')
    plt.ylabel('The Normalized Stock Price')
    plt.show()
        