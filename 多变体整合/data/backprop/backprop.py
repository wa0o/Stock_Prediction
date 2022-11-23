
def backprop_experiment():
    from data import sample
    from backprop import net_params
    from backprop import net
    import numpy as np
    import matplotlib.pyplot as plt

    par = net_params.net_params()

    sam = sample.test_sample()
    sam.get_back_sample(par)
    sam.get_test_sample(par)

    network = net.network()

    signalsample = sample.sample(sam.train_input[0],sam.train_output[0])
    network.weight_initialize(par)
    network.node_size_initialize(signalsample,par)


    for i in range(len(sam.train_output)):
        signalsample = sample.sample(sam.train_input[i],sam.train_output[i])
        ans = network.node_update(signalsample,par)
        network.errors_update(signalsample,ans)
        network.weight_update(par.learing_rate)
        if i %50 == 0:
            if i%500==0:
                par.learing_rate *=(1-par.learing_decat)
                print(i)
            plt.plot(i,abs(ans-signalsample.output),marker = '.',color='coral')
            plt.ylabel('error')
            plt.draw()
            plt.pause(0.01)

        
    for i in range(len(sam.test_output)):
        signalsample = sample.sample(sam.test_input[i],sam.test_output[i])
        ans = network.node_update(signalsample,par)
        print(ans,signalsample.output)