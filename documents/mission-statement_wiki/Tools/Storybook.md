- install node.js to have npx

```
# Create our application:
npx create-react-app taskbox

cd taskbox

# Add Storybook:
npx -p @storybook/cli sb init

# Run the test runner (Jest) in a terminal:
yarn test --watchAll

# Start the component explorer on port 9009:
yarn storybook

# Run the frontend app proper on port 3000:
yarn start
```
