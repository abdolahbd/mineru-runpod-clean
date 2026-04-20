import runpod

def handler(job):
    return {
        "success": True,
        "message": "worker is alive",
        "input": job.get("input", {})
    }

runpod.serverless.start({"handler": handler})