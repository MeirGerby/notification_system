from fastapi import FastAPI
import dal
app = FastAPI()


@app.get("/analytics/alerts-by-border-and-priority")
async def alerts_by_border_and_priority():
    return dal.alerts_by_border_and_priority()

@app.get(" /analytics/top-urgent-zones")
async def top_urgent_zones():
    return dal.top_urgent_zones()

@app.get("/analytics/distance-distribution")
async def distance_distribution():
    return dal.distance_distribution()

@app.get("/analytics/low-visibility-high-activity")
async def low_visibility_high_activity():
    return dal.low_visibility_high_activity()

@app.get("/analytics/hot-zones")
async def hot_zones():
    return dal.hot_zones()