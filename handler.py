import runpod

def my_handler(job):
    job_input = job['input']
    name = job_input.get('name', 'World')
    return {"message": f"Hello {name} from RunPod! Worker is running successfully."}

runpod.serverless.start({"handler": my_handler})
