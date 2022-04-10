# ROS-Turtlebot-Project
ROS And AI Project Under YTÜ Mint AI 

## Ros nedir?

![ros-nedir](https://user-images.githubusercontent.com/59237081/162614341-05088347-cd81-4ce5-baff-f4ac6883a3b5.jpeg)

Robot İşletim Sistemi robot yazılımı geliştiricileri için işletim sistemi sağlayan bir yazılım iskeletidir. İsminde işletim sistemi ifadesi geçse de insan ile robot arasında iletişimi sağlayan açık kaynak kodlu bir arayüz yazılımı denebilir. ROS, robotlarda oldukça yaygın olarak kullanılan yazılımdır.Robotun dış dünyadan sensörler aracığıyla aldığı verileri işleyip tekrar robota komut olarak göndermeyi sağlayan arayüzdür. Daha fazla bilgiyi https://wiki.ros.org/ROS/Introduction sitesinden alabilirsiniz.

## Gazebo Nedir?

![221-2216011_ros-gazebo-logo](https://user-images.githubusercontent.com/59237081/162616496-16b812e9-01f0-40b0-9919-f0a652a92c30.jpeg)

<img width="1012" alt="Ekran Resmi 2022-04-10 15 12 30" src="https://user-images.githubusercontent.com/59237081/162617460-7a54caae-4fa2-4a23-9ede-c88d2f00f127.png">


Bu eğitim, robotik senaryolarının gerçekçi simülasyonlarına sahip olmak isteyen robot uzmanlarına yöneliktir. Gazebo bir 3D simülatördür, ROS ise robot için arayüz görevi görür. Her ikisini birleştirmek, güçlü bir robot simülatörü ile sonuçlanır.

Gazebo ile robotlar, engeller ve daha birçok nesne ile bilgisayarınızda 3 boyutlu bir senaryo oluşturabilirsiniz. Gazebo ayrıca aydınlatma, yerçekimi, atalet vb. için fiziksel bir motor kullanır. Robotunuzu zor veya tehlikeli senaryolarda robotunuza zarar vermeden değerlendirebilir ve test edebilirsiniz. Çoğu zaman, tüm senaryoyu gerçek robotunuzda başlatmak yerine bir simülatör çalıştırmak daha hızlıdır.

Aslen Gazebo, robotlar için algoritmaları değerlendirmek için tasarlandı. Hata işleme, pil ömrü, konum belirleme, gezinme ve kavrama gibi birçok uygulama için robot uygulamanızı test etmeniz önemlidir. Çok robotlu bir simülatöre ihtiyaç duyulduğundan Gazebo geliştirildi.

## Rviz Nedir?

![splash](https://user-images.githubusercontent.com/59237081/162616422-8fc14c15-2330-4a81-835b-000fe08830c6.png)


Rviz, Ros uygulamaları için bir 3D görselleştirme ortamıdır. Robot modelinin görünümünü sağlamasının yanı sıra sensör bilgilerinin kaydedilmesi ve görselleştirilmesi, geliştirme ve hata ayıklama için önemli bir araçtır. Robotun ne gördüğünü ve ne yaptığını görmemizi sağlar. Resimler ve point cloud verileri dahil olmak üzere kameradan, lidarlardan, 3D ve 2D cihazlardan gelen verileri görüntüleyebilir.

## TurtleBot nedir?

![ros-robot](https://user-images.githubusercontent.com/59237081/162614572-bb09bf2b-46ea-434f-81d0-3db233d00604.png)

Turtlebot 3 modüler, kompakt ve özelleştirilebilir yeni nesil bir mobil robottur. Robotun amacı kapasiteyi, işlevselliği ve kaliteyi ödün vermeden platformun boyutunu önemli ölçüde azaltmak ve fiyatını düşürmektir. Turtlebot 3, Open Robotics, Robotis ve İntel, Onshape, Oroca gibi daha fazla ortak arasında iş birliği projesidir.

## Ros'un çalışma mantığı nedir?!

<img width="805" alt="Ekran Resmi 2022-04-10 13 58 07" src="https://user-images.githubusercontent.com/59237081/162614849-0870a711-0da5-4ad3-a7f3-3639aaffa6ac.png">


 Buradaki çalışma mantığı yayınlama/abone yani daha basit anlamda alıcı-gönderici mantığında çalışmaktadır. Bilgisayar ile root arasındaki bu iletişim topic’ler ve mesajlar sayesinde sağlanmaktadır. Açık kaynak kodlu(BSD) bir sistemdir. Programlama dili olarak bağımsız olarak nitelendirilebilir. Aynı robot üzerinde farklı diller(java, lisp, c++, pyhton) kullanmaya izin verir. 


# Proje

### Kodu çalıştırma
3 Adet terminal açılır ve her bir terminale alttaki kodlar yazılır.
* 1.Terminale: roscore    <br> # Ros çekirdeğini başlatmak
* 2.Terminale: roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch          <br> # turtlebot3 robotumuzu boş bir dünya'ya koymak ve Gazebo'yu başlatmak
* 3.Terminale: rosrun basit_uygulamalar main.py       <br>    # py dosyamız catkin_ws/src altında bulunan basit_uygulamalar adlı workspace'de bulunmakta, main.py ise scripts klasörünün altında, bu py dosyasını çalıştırarak programı başlatıyoruz.

