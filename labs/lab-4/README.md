Lab-4
======

Sarthak Kaushik(101471600)
---------------------------

Structure of the `lab-4` dir
----------------------------

- Design rationale document is in the `design-document` dir.
- All screenshots are in the `images` dir.
- All the YAMLs are in the `k8s-yaml-files` dir.


Architecture Diagram
----------------------------

![architecture](./design-document/k8s-design-doc.drawio.png)


Design Document
----------------------------

[Cick to view the Design Document](./design-document/DesignDocument.pdf)

Starting minikube with 16 cores and 48 GiB RAM
------------------------------------------------

1. ![1.png](./images/dashboard/1.png)


Dashboard after full deployment
--------------------------------

2. ![2.png](./images/dashboard/2.png)
3. ![3.png](./images/dashboard/3.png)
4. ![4.png](./images/dashboard/4.png)
5. ![5.png](./images/dashboard/5.png)

Services
----------

6. ![6.png](./images/dashboard/6.png)

ConfigMaps
----------


7. ![7.png](./images/dashboard/7.png)

PVCs
------

8. ![8.png](./images/dashboard/8.png)

Secrets
--------

9. ![9.png](./images/dashboard/9.png)


Storage Classes
-----------------


10. ![10.png](./images/dashboard/10.png)

Cluster Role Bindings
-----------------------

11. ![11.png](./images/dashboard/11.png)

Cluster Roles
--------------

12. ![12.png](./images/dashboard/12.png)


Namespaces
-----------


13. ![13.png](./images/dashboard/13.png)

Nodes
-------

14. ![14.png](./images/dashboard/14.png)


PVs
-----

15. ![15.png](./images/dashboard/15.png)

Role Bindings
--------------

16. ![16.png](./images/dashboard/16.png)


Roles
--------

17. ![17.png](./images/dashboard/17.png)


Service Accounts
------------------

18. ![18.png](./images/dashboard/18.png)


All services
-------------

18. ![18.png](./images/all.png)



Forwarding pods from K8s to make the services accessible on `localhost` and facilitate inter-service communication
--------------------------------------------------------------------------------------------------------------------

18. ![18.png](./images/port-forward/1.png)
18. ![18.png](./images/port-forward/2.png)


ReplicaSet
-------------

The replicas of the pods are shown, the cluster will maintain atleast the 
declared number of copies of these (here 3).

1. ![4.png](./images/replica-set/1.png)

Storage
---------

Using PVC to write the message to a file:

1. ![4.png](./images/pvc/1.png)
2. ![4.png](./images/pvc/2.png)
1. ![4.png](./images/pvc/3.png)


Scaling
---------

Horizontal pod autoscaling technique is used.

1. ![4.png](./images/scaling/1.png)


Load Balancing
---------------


This has been achieved using the `spec` attribute's type of `LoadBalancing`.

1. ![4.png](./images/load-balancer/1.png)

Secrets
---------


1. ![4.png](./images/secret/1.png)


Config Map
------------

1. ![4.png](./images/secret/config-map.png)


RBAC
-------

1. Client certificate for the user:

![img.png](./images/roles/img.png)

2. User entry in kubeconfig:

![img.png](./images/roles/img_1.png)

3. Context entry in kubeconfig:

![img.png](./images/roles/img_2.png)

4. Switched to the created user:

![img.png](./images/roles/img_3.png)

![img.png](./images/roles/img_4.png)


5. Role Creation with read-only access

![img.png](./images/roles/img_5.png)

6. Binding the Role to the user sarthak

![img.png](./images/roles/img_6.png)

![img.png](./images/roles/img_7.png)

Docker Ethereum App UI
----------------------

1. ![4.png](./images/app/1.png)
1. ![4.png](./images/app/2.png)
1. ![4.png](./images/app/3.png)













































































































































































































































































































