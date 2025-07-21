config_a = {"lr": 0.01, "epochs": 10}
config_b = {"batch_size": 32, "lr": 0.001}

# Merge (config_b overrides config_a)
final_config = {**config_a, **config_b}
finalss_config = {**config_b, **config_a}


print("Merged Config:", final_config)
print("Final Config:", finalss_config)
