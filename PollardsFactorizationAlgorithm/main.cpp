#include <iostream>
#include <cstdlib>
#include <time.h>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

unsigned long long n, k = 1, d, a;
unsigned int B;
string result = "FAILURE";

int randomNumberGenerator(int lowerBound, int upperBound)
{
    srand(time(NULL));
    return rand() % upperBound + lowerBound;
}

bool verifyIfPrime(unsigned int q)
{
    for (unsigned int d = 2; d <= q / 2; d++)
    {
        if (q % d == 0)
        {
            return false;
        }
    }
    return true;
}
unsigned long long calculateProduct()
{
    unsigned int i, q = 2;
    unsigned long long p;
    while (q <= B)
    {
        i = 1;
        if (verifyIfPrime(q))
        {
            while (pow(q, i) <= B)
            {
                i++;
            }
            p = pow(q, (i - 1));
            //cout << "p = " << p << "\n";
            k *= p;
        }
        q++;
    }
    return k;
}

unsigned long long lcm(unsigned int lowerBound, unsigned int upperBound)
{
    return 0;
}

unsigned long long gcd(unsigned long long a, unsigned long long b)
{
    unsigned long long r;
    while (b > 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

vector<unsigned int> binaryFactorization(unsigned int k)
{
    vector<unsigned int> binaryFactorizationK = vector<unsigned int>();
    while (k >= 1)
    {
        binaryFactorizationK.push_back((k % 2));
        k /= 2;
    }
    return binaryFactorizationK;
}

unsigned long long repeatedSquareModularExponentiation(unsigned int b, unsigned long long k, unsigned long long n)
{
    vector<unsigned int> binaryFactorizationK = binaryFactorization(k);
    unsigned long long a = 1;
    unsigned long long aux = b;
    if (k == 0)
    {
        return a;
    }
    if (binaryFactorizationK.at(0) == 1)
    {
        a = b;
    }
    for (unsigned int i = 1; i < binaryFactorizationK.size(); i++)
    {
        aux = (aux * aux) % n;
        //cout << "aux = " << aux << "\n";
        if (binaryFactorizationK.at(i) == 1)
        {
            a *= aux;
            a = a % n;
        }
    }
    //cout << "a = " << a << "\n";
    return a;
}

int main()
{
    unsigned long long ak;
    cout << "Input n: ";
    cin >> n;
    cout << "Input the bound: ";
    cin >> B;
    k = calculateProduct();
    //cout << "k = " << k << "\n";
    while (result.compare("FAILURE") == 0)
    {
        a = randomNumberGenerator(2, n - 2);
        //a = 2;
        cout << "a = " << a << "\n";
        ak = repeatedSquareModularExponentiation(a, k, n);
        cout << "ak = " << ak << "\n";

        d = gcd((ak - 1), n);
        if (d == 1 || d == n)
        {
            cout << result << "\n";
        }
        else
        {
            result = "SUCCESS";
            cout << result << "\n";
            cout << "d = " << d << "\n";
        }
    }
}