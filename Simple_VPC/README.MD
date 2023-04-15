
##### Simple VPC use case

* Created a VPC in GCP.
* Created two subnetworks.

--> subnetwork1 ---- 10.0.0.0/24

--> subnetwork2 ---- 10.0.1.0/24

Created three instances to check the connections between the instances.

--> instance1, instance2 ---- subnetwork1

--> instance3            ---- subnetwork2

* At first instance1 was not able to make a connection to instance2 and instance3
* Then created a separate firewall rule to enable the connection and able to connect between those instances.


![VPC Diagram](https://github.com/Senthuran100/GCP_HandsOn/blob/main/Simple_VPC/VPC.drawio.png)