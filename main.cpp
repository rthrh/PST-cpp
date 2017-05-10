#include <iostream>
#include <vector>


void meshgrid(std::vector<double> x, std::vector<double> y, std::vector<std::vector<double> > Xout, std::vector<std::vector<double> > Yout)
{
    std::vector<std::vector<double> >::iterator itx;
    std::vector<std::vector<double> >::iterator ity;


    for(int i=0; i < y.size()-1; ++i)
        itx = Xout.begin();
        Xout.insert ( itx , x );

    for(int i=0; i < x.size()-1; ++i)
        ity = Yout.begin();
        Yout.insert ( ity , y );

}




template<typename T>
std::vector<double> linspace(T start_in, T end_in, int num_in)
{

  std::vector<double> linspaced;

  double start = static_cast<double>(start_in);
  double end = static_cast<double>(end_in);
  double num = static_cast<double>(num_in);

  if (num == 0) { return linspaced; }
  if (num == 1)
    {
      linspaced.push_back(start);
      return linspaced;
    }

  double delta = (end - start) / (num - 1);

  for(int i=0; i < num-1; ++i)
    {
      linspaced.push_back(start + delta * i);
    }
  linspaced.push_back(end); // I want to ensure that start and end
                            // are exactly the same as the input
  return linspaced;
}

void print_vector(std::vector<double> vec)
{
  std::cout << "size: " << vec.size() << std::endl;
  for (double d : vec)
    std::cout << d << " ";
  std::cout << std::endl;
}

void print_vector_of_vectors(std::vector<std::vector<double> > vec)
{
    std::cout << "lets start" << std::endl;
    for (int i = 0; i < vec.size(); i++)
    {
        for (int j = 0; j < vec[i].size(); j++)
        {
            std::cout << "hi there" << std::endl;
            std::cout << vec[i][j];
        }
    }
}

int main()
{
    double l = 0.5;
    std::vector<double> vec_1 = linspace(-l, l, 6);
    //print_vector(vec_1);
    std::vector<double> vec_2 = linspace(-l, l, 12);
    //print_vector(vec_2);
///////

    std::vector<std::vector<double> > X(vec_1.size());
    std::vector<std::vector<double> > Y(vec_2.size());

    meshgrid(vec_1,vec_2,X,Y);

    cout << "sizes /n/n/n" << endl;



    print_vector_of_vectors(X);
    ////////////////////

    return 0;
}
