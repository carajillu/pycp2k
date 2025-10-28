from dask.distributed import Client, LocalCluster
def create_cluster(n_workers: int=4, threads_per_worker: int=2):
    cluster = LocalCluster(n_workers=n_workers, threads_per_worker=threads_per_worker)
    return cluster