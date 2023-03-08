#include <stdio.h>
#include <stdlib.h>
#include<ctype.h>

int main()
{
   FILE *fichier;
   char nom_fichier[] = "mon_fichier.txt";
   int compteur = 0, nombre = 5;

   fichier = fopen(nom_fichier, "r");
   if (fichier == NULL) {
      printf("Impossible d'ouvrir le fichier.\n");
      return 1;
   }

   while (fscanf(fichier, "%d", &nombre) == 1)
   {
      printf("Le nombre est %d", nombre);
      
         compteur++;
      
   }

   fclose(fichier);
   printf("Le fichier contient %d entiers naturels.\n", compteur);
   return 0;
}
/*FILE * f = NULL;
 int c ;
 f = fopen ( "mon_fichier.txt" , "r" ) ;
if ( f != NULL) {
 c = fgetc ( f ) ;
 printf("%c\n",c);

 while ( c != EOF)
    {
//putchar(c) ;
c = fgetc(f) ;
 printf("%c\n",c);
 }
 //printf("%c\n",c);
 fclose(f)  ;
 }
else
printf ( " Impossible d�ouvrir le fichier \n" );*/
