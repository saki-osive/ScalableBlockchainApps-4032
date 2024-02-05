Lab-5
======

Sarthak Kaushik(101471600)
---------------------------

Install Prometheus
-----------------------

* Cluster Start
  ![img](./images/img.png)

* Helm Install
  ![img](./images/img_1.png)

  ![img](./images/img_2.png)

* Added helm repo
  ![img](./images/img_3.png)

* Install helm
  ![img](./images/img_6.png)

* Service
  ![img](./images/img_4.png)

* Pods
  ![img](./images/img_5.png)

* Expose Prometheus Server
  ![img](./images/img_7.png)

* Dashboard
  ![img](./images/img_8.png)

Install Grafana
-----------------------

* Add Helm Repo
  ![img](./images/img_9.png)

* Update Helm Repo
  ![img](./images/img_10.png)

* Install Helm
  ![img](./images/img_11.png)

* Expose Grafana Service
  ![img](./images/img_12.png)

* Get Grafana admin password
  ![img](./images/img_13.png)

* Login using the generated admin password
  ![img](./images/img_14.png)

* Dashboard after Login
  ![img](./images/img_15.png)

* Pods
  ![img](./images/img_16.png)

* Service
  ![img](./images/img_17.png)


Connect Prometheus as Data source to Grafana
---------------------------------------------

1. Clicked on Add new Data Source
   ![img](./images/img_19.png)

1. Selected Prometheus
   ![img](./images/img_18.png)

3. Provided Server URL
   ![img](./images/img_20.png)

4. Clicked on ``Save & test``
   ![img](./images/img_21.png)
   ![img](./images/img_22.png)

Create a custom dashboard with 3 visualizations of your choice displaying information about the minikube kubernetes cluster running on your system.
----------------------------------------------------------------------------------------------------------------------------------------------------------

1. Clicked on ``building a Dashboard``
   ![img](./images/img_23.png)

2. Clicked on ``Add Visualisation``
   ![img](./images/img_24.png)

3. Selected the previously added Prometheus Datasource
   ![img](./images/img_25.png)

4. Sample Dashboard
   ![img](./images/img_28.png)

Importing a Dashboard

1. Clicked on ``Import Dashboard``
   ![img](./images/img_24.png)

2. Provided 3662 ID
   ![img](./images/img_26.png)

3. Selected Prometheus as Data Source and Clicked Import
   ![img](./images/img_27.png)

Grafana Dashboard
--------------------

![img](./images/img_29.png)

![img](./images/img_30.png)

![img](./images/img_31.png)

![img](./images/img_32.png)

![img](./images/img_33.png)





















