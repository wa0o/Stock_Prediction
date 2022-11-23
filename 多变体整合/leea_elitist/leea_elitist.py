from cgitb import small


def leea_experiment():
    from data import sample
    from leea_elitist import net_params
    from leea_elitist import net
    from leea_elitist import function
    import numpy as np
    import matplotlib.pyplot as plt
    from multiprocessing import Pool


    params = net_params.net_params()

    test = sample.test_sample()
    test.get_leea_sample(params)
    test.get_test_sample(params)

    sample_list = []
    for i in range(len(test.train_output)):
        tmp = sample.sample(test.train_input[i],test.train_output[i])
        sample_list.append(tmp)


    species = net.create_first_generation(params)
    small_species = []
    for i in range(params.process_num):
        small_species.append(function.divide(species,params,i))
    for i in range(params.process_num):
        small_species[i] = function.evaluate_all(small_species[i],sample_list,params)
    pool = Pool(processes=params.process_num)
    tmp = []
    for i in range(params.process_num):
        one = pool.apply_async(net.evolve,args=(small_species[i],params))
        tmp.append(one)
    pool.close()
    pool.join
    new_species = []
    for one in tmp:
        new_species.extend(one.get())

    for i in range(len(test.test_output)):
        tmp = sample.sample(test.test_input[i],test.test_output[i])
        sample_list.append(tmp)
        
    new_species.sort(key = function.getfitness,reverse=True)
    x2 = np.arange(0.0, len(sample_list), 1.0)
    z2 = np.arange(0.0, len(sample_list), 1.0)
    z3 = np.arange(0.0, len(sample_list), 1.0)
    
    i = 0
    for sam in sample_list:
        ans = function.node_update(sam,new_species[0])
        z2[i] = ans
        z3[i] = sam.output
        print('predict:',ans,'fact:',sam.output)
        i += 1

    plt.plot(x2, z2, x2, z3)
    plt.title('LEEA-predict-fact')
    plt.show()