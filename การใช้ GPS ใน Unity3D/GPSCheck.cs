using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Linq;
using UnityEngine.SceneManagement;
public class GPSCheck : MonoBehaviour {

	private double[] t1Lat1 = { 12.073144, 12.073072, 12.073142, 12.073066 },
        t1Long1 = { 98.977573, 98.977581, 98.977794, 98.97794 },
        t1Lat2 = { 12.073142, 12.073066, 12.073152, 12.073070 },
        t1Long2 = { 98.977794, 98.977794, 98.978003, 98.978015 },
        t1Lat3 = { 12.073152, 12.073070, 12.073150, 12.073056 },
        t1Long3 = { 98.978003, 98.978015, 98.978198, 98.978208 };
		
    public float lat, lon;
    private float minLat = 9999999.00f, maxLat = -1.0f, minLong = 9999999.00f, maxLong = -1.0f;
	
    void Start () {
        minLat = (float)pbruLat.Min();
        maxLat = (float)pbruLat.Max();
        minLong = (float)pbruLong.Min();
        maxLong = (float)pbruLong.Max();
    }
	
	void Update () {
		lat = GPS.Instance.latitude;
        lon = GPS.Instance.longitude;
		
		if ((lat <= t1Lat1.Max() && lat >= t1Lat1.Min() && lon <= t1Long1.Max() && lon >= t1Long1.Min()) ||
                (lat <= t1Lat2.Max() && lat >= t1Lat2.Min() && lon <= t1Long2.Max() && lon >= t1Long2.Min()) ||
                (lat <= t1Lat3.Max() && lat >= t1Lat3.Min() && lon <= t1Long3.Max() && lon >= t1Long3.Min()))
            {
				//do something
			}
	}
}
