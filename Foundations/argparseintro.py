import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say a Greeting.")
    parser.add_argument('name', type=str)
    parser.add_argument('--city', type=str,
                        default="San Fran", help="where is the person from?")

    args = parser.parse_args()
    name = args.name
    city = args.city
    print(f'Hello, {name} from {city}')

    name = sys.argv[1]
    city = sys.argv[2]

    print(f'hello, {name} from {city}')

