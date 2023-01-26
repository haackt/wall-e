export default function getRandomNumber(minimumNumber: number, maximumNumber: number): number {
  return Math.round(Math.random() * (maximumNumber - minimumNumber) + minimumNumber);
}
