string[] FillArray(int size)
{
  string[] testArray = new string[size];
  Random nr = new Random();
  for (int i = 0; i < size; i++)
    testArray[i] = Convert.ToString(nr.Next(0, 10000));
  return testArray;
}

string[] GetStringsWithRequiredLength(string[] inputArray, int maxLength)
{
  string[] resultArray = new string[inputArray.Length];
  int j = 0;
  for (int i = 0; i < inputArray.Length; i++)
  {
    if (inputArray[i].Length <= maxLength)
    {
      resultArray[j] = inputArray[i];
      j++;
    }
  }
  Array.Resize(ref resultArray, j);
  return resultArray;
}

string[] sourceArray = FillArray(50);
string[] resultString = GetStringsWithRequiredLength(sourceArray, 3);
Console.WriteLine($"{string.Join(", ", resultString)}");