from dask.distributed import Client, LocalCluster
def create_cluster(n_workers: int=1, threads_per_worker: int=1,scale=1):
    """
    create a Dask local cluster. For external binaries, we use 
    n_workers=1 and threads_per_worker=1 and handle the number of
    concurrent tasks with cluster.scale()
    """
    cluster = LocalCluster(n_workers=n_workers, threads_per_worker=threads_per_worker)
    cluster.scale(scale)
    return cluster