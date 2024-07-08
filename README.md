# Optimisation_transport_livraison
 Résolution des problèmes de transport
 
Introduction

 La question des problèmes de transport est intimement liée aux questions sociales, économiques ou
 écologiques. A travers les algorithmes vus en cours, nous cherchons à comprendre comment abaisser
 les coûts de transports dans un réseau. La nature de ces coûts peut être humaine, monétaire ou liée à
 l’environnement.
 Dans ce projet, il est question de la rédaction d’un programme qui résout un problème de transport.
 Une fois le code construit, nous vous demanderons de le tester sur les problèmes qui se trouvent en
 annexes et dont il faudra nous fournir les traces d’exécution. Enfin, si et seulement si votre programme
 fonctionne parfaitement, vous pourrez l’utiliser afin d’analyser la complexité générée.

 Le problème à résoudre

  Nous vous demandons de coder la résolution du problème suivant : soient n fournisseurs ayant des
 provisions, appelées (Pi)i∈[[1;n]] et m clients ayant fait des commandes, appelées (Cj)j∈[[1;m]]. Chaque
 transport unitaire d’un objet entre le fournisseur i et le client j coûte ai,j, ce qui forme la matrice
 A=(ai,j)(i,j)∈[[1;n]]×[[1;m]].
 L’objectif est de trouver la meilleure façon de transporter les objets des fournisseurs vers les
 clients qui minimise le coût total du transport. C’est à dire que l’on cherche à trouver les nombres
 (bi,j)(i,j)∈[[1;n]]×[[1;m]] d’objet transportés depuis chaque fournisseur i vers chaque client j tels que
 2
1.2Lecode 3
 ∑n
 i=1∑m
 j=1ai,j×bi,j soitminimal,souslacontraintedesprovisions∑m
 j=1bi,j=Pietdescommandes
 ∑n
 i=1bi,j=Cj.Ils’agitbienévidemmentduproblèmeétudiéencours
