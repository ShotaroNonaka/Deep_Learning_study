import gym

import nnabla_rl.algorithms as A
import nnabla_rl.hooks as H
import nnabla_rl.writers as W
from nnabla_rl.utils.evaluator import EpisodicEvaluator

# save training computational graph
training_graph_hook = H.TrainingGraphHook(outdir="test")

# evaluation hook with nnabla's Monitor
eval_env = gym.make("Pendulum-v1")
evaluator = EpisodicEvaluator(run_per_evaluation=10)
evaluation_hook = H.EvaluationHook(
    eval_env,
    evaluator,
    timing=10,
    writer=W.MonitorWriter(outdir="test", file_prefix='evaluation_result'),
)

env = gym.make("Pendulum-v1")
sac = A.SAC(env)
sac.set_hooks([training_graph_hook, evaluation_hook])

sac.train_online(env, total_iterations=100)