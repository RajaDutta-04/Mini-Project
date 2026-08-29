#include <stdio.h>
#include <GL/glut.h>

void myInit(){
    glClearColor(0.4,0.4,0.4,0.0);
    glColor3f(0.0f,0.0f,0.0f);
    glPointSize(10.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,380,420,0);

}

void myDisplay(){
    glClear(GL_COLOR_BUFFER_BIT);

    FILE* fptr = fopen("output.txt","r");
    if(!fptr) return;

    char line[250];
    int y = 4;

    glBegin(GL_POINTS);
    int scale = 10;
    
    while(fgets(line,sizeof(line),fptr)){
        int x = 4;
        for(int i=0; line[i] != '\0'; i++){
            if(line[i] == '1'){
                glColor3f(0.0f,0.0f,0.0f);
                glVertex2i(x,y);
            }if(line[i] == '0'){
                glColor3f(1.0f,1.0f,1.0f);
                glVertex2i(x,y);
            }
            x+=10;
        }
        y+=10;
    }

    glEnd();
    fclose(fptr);
    glFlush();
}
// Function to convert decimal to binary and write to file
void writeBinary(FILE *out, char num[])
{
    char temp[200];
    strcpy(temp,num);

    int len;
    int remainder;
    int binary[500];
    int k = 0;

    while(!(strlen(temp)==1 && temp[0]=='0'))
    {
        remainder = 0;
        char next[200];
        int j = 0;

        for(int i=0;i<strlen(temp);i++)
        {
            int digit = remainder*10 + (temp[i]-'0');
            next[j++] = (digit/2) + '0';
            remainder = digit%2;
        }

        next[j]='\0';

        if(next[0]=='0' && strlen(next)>1)
            memmove(next,next+1,strlen(next));

        binary[k++] = remainder;

        strcpy(temp,next);
    }

    for(int i=k-1;i>=0;i--)
        fprintf(out,"%d",binary[i]);
}

int main(int argc,char** argv) {
    FILE *input = fopen("input2.txt", "r");
    FILE *output = fopen("output.txt", "w");

    if (input == NULL) {
        printf("Error: Cannot open input file.\n");
        return 1;
    }

    char num[200];

while(fscanf(input,"%s",num)==1){
    writeBinary(output,num);
    fprintf(output,"\n");
}

    fclose(input);
    fclose(output);

    printf("Conversion completed. Check output.txt\n");
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowPosition(100,150);
    glutInitWindowSize(390,420);
    
    glutCreateWindow ("Space Time Diagram");
    glutDisplayFunc(myDisplay);
    myInit();
    glutMainLoop();
    return 0;
}
// gcc code.c -lfreeglut -lopengl32 -lglu32