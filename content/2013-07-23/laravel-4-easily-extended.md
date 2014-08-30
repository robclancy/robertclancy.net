title: Laravel 4 - Easily Extended
tags: php, laravel, hashing

I recently [replaced some Laravel functionality](https://github.com/robclancy/laravel4-hashing) for someone who was forced to use [Laravel 4](http://laravel.com) on a shared host which didn’t have PHP up to date. I thought this would be a good time to explain one of the advantages of the component based architecture of Laravel 4 and how I was able to drop the PHP requirement to 5.3.2 in less than an hour.

Laravel 4 uses [Bcrypt](http://en.wikipedia.org/wiki/Bcrypt), [as it should](http://www.codinghorror.com/blog/2012/04/speed-hashing.html). More accurately, it uses [Anthony Ferrara’s](https://twitter.com/ircmaxell) [password_compat](https://github.com/ircmaxell/password_compat#password_compat) library which brings PHP 5.5 [password functionality](https://wiki.php.net/rfc/password_hash) (of which he [designed](http://blog.ircmaxell.com/2012/11/designing-api-simplified-password.html) and proposed the specification for) to PHP 5.3.7+. Therefore the minimum PHP requirement for Laravel 4 is the same as password_compat. This is the only thing pushing the requirement past 5.3.2 so I just had to replace that functionality.

I am going to go step by step through how I made the package as an overview on creating packages for Laravel and to show you how little I needed to change for this to work.

When I start with any package I first create my repository on github and clone it. Then comes the generic directory structure I always use which is as follows.

    /src
        /Robbo
    /tests
    .gitignore
    .travis.yml
    README.md
    composer.json
    phpunit.xml

The root files here are generally the same except for composer.json. You can copy them from any of my packages if need be.

Now we need something to do the actual hashing, luckily Anthony has us covered there too with [PHP-PasswordLib](https://github.com/ircmaxell/PHP-PasswordLib#about). I just add it to composer.json under require with "PasswordLib/PasswordLib": “*”. After which you will need to do a composer update. This is now ready to go, composer will handle the autoloading. 

Next is the new implementation of Illuminate\Hashing\HasherInterface. I am going to be using the Sha512 Hash function, however the library will be expanded in future to support more of [hash functions](https://github.com/ircmaxell/PHP-PasswordLib#specifications) provided by PHP-PasswordLib.

It starts off in src/Robbo/Hashing/Sha512Hasher.php as...

    <?php namespace Robbo\Hashing;
    
    use PasswordLib\PasswordLib;
    use Illuminate\Hashing\HasherInterface;
    
    class Sha512Hasher implements HasherInterface {
    
    }

Now we can just copy paste the contents from Illuminate\Hashing\HasherInterface.

    <?php namespace Robbo\Hashing;
    
    use PasswordLib\PasswordLib;
    use Illuminate\Hashing\HasherInterface;
    
    class Sha512Hasher implements HasherInterface {
    
        /**
         * Hash the given value.
         *
         * @param  string  $value
         * @return array   $options
         * @return string
         */
        public function make($value, array $options = array());
    
        /**
         * Check the given plain value against a hash.
         *
         * @param  string  $value
         * @param  string  $hashedValue
         * @param  array   $options
         * @return bool
         */
        public function check($value, $hashedValue, array $options = array());
    
        /**
         * Check if the given hash has been hashed using the given options.
         *
         * @param  string  $hashedValue
         * @param  array   $options
         * @return bool
         */
        public function needsRehash($hashedValue, array $options = array());
    }

We need a PasswordLib instance now. So create it in the constructor for later use.

    <?php namespace Robbo\Hashing;
        
    use PasswordLib\PasswordLib;
    use Illuminate\Hashing\HasherInterface;
    
    class Sha512Hasher implements HasherInterface {
    
        protected $hasher;
    
        /**
         * Create a new Sha512 hasher instance.
         *
         * @return void
         */
        public function __construct()
        {
            $this->hasher = new PasswordLib;
        }
    
        /**
         * Hash the given value.
         *
         * @param  string  $value
         * @return array   $options
         * @return string
         */
        public function make($value, array $options = array());
    
        /**
         * Check the given plain value against a hash.
         *
         * @param  string  $value
         * @param  string  $hashedValue
         * @param  array   $options
         * @return bool
         */
        public function check($value, $hashedValue, array $options = array());
    
        /**
         * Check if the given hash has been hashed using the given options.
         *
         * @param  string  $hashedValue
         * @param  array   $options
         * @return bool
         */
        public function needsRehash($hashedValue, array $options = array());
    
    }

Now all we need to do is fill out the methods and the hasher should work anywhere in Laravel without issue.

The make method will make a simple call to PasswordLib to create the Sha512 hash. It uses '$6$' to identify as Sha512.

    /**
     * Hash the given value.
     *
     * @param  string  $value
     * @return array   $options
     * @return string
     */
    public function make($value, array $options = array())
    {
        return $this->hasher->createPasswordHash($value, '$6$', $options);
    }

Then for the check method it is another single call to PasswordLib. It does all the heavy lifting making this a second very simple line of code.

    /**
     * Check the given plain value against a hash.
     *
     * @param  string  $value
     * @param  string  $hashedValue
     * @param  array   $options
     * @return bool
     */
    public function check($value, $hashedValue, array $options = array())
    {
        return $this->hasher->verifyPasswordHash($value, $hashedValue);
    }

Lastly, we aren’t supporting rehashing so just return false for that method (I might support it in future if required). Here is the Hasher fully implemented. 

    <?php namespace Robbo\Hashing;
    
    use PasswordLib\PasswordLib;
    use Illuminate\Hashing\HasherInterface;
    
    class Sha512Hasher implements HasherInterface {
    
        protected $hasher;
    
        /**
         * Create a new Sha512 hasher instance.
         *
         * @return void
         */
        public function __construct()
        {
            $this->hasher = new PasswordLib;
        }
    
        /**
         * Hash the given value.
         *
         * @param  string  $value
         * @return array   $options
         * @return string
         */
        public function make($value, array $options = array())
        {
            return $this->hasher->createPasswordHash($value, '$6$', $options);
        }
    
        /**
         * Check the given plain value against a hash.
         *
         * @param  string  $value
         * @param  string  $hashedValue
         * @param  array   $options
         * @return bool
         */
        public function check($value, $hashedValue, array $options = array())
        {
            return $this->hasher->verifyPasswordHash($value, $hashedValue);
        }
    
        /**
         * Check if the given hash has been hashed using the given options.
         *
         * @param  string  $hashedValue
         * @param  array   $options
         * @return bool
         */
        public function needsRehash($hashedValue, array $options = array())
        {
            return false;
        }
    
    }

Now we have our hasher implementation sorted. What’s next? Well how do we know if it even works? Let’s make a test. Create the test file at tests/Sha512HasherTest.php and test the 2 methods we are using.

    <?php
    
    class Sha512HasherTest extends PHPUnit_Framework_TestCase {
    
        public function testBasicHashing()
        {
            $hasher = new Robbo\Hashing\Sha512Hasher;
            $value = $hasher->make('password');
            $this->assertTrue($value !== 'password');
            $this->assertTrue($hasher->check('password', $value));
            $this->assertFalse($hasher->check('wrongpassword', $value));
        }
    }

Lastly we need to tell laravel to use the new Hasher. For this situation I decided to just extend Illuminate\Hashing\HashServiceProvider to register the new Hasher. This class simply contains yet another single line method.

    <?php namespace Robbo\Hashing;
    
    use Illuminate\Hashing\HashServiceProvider as ServiceProvider;
    
    class HashServiceProvider extends ServiceProvider {
    
        /**
         * Register the service provider.
         *
         * @return void
         */
        public function register()
        {
            $this->app['hash'] = $this->app->share(function() { return new Sha512Hasher; });
        }
    }

To get this working from here you simply replace Illuminate\Hashing\HashServiceProvider with Robbo\Hashing\HashServiceProvider in app/config/app.php... that is it. So installation is 2 file edits. You add the dependency to composer.json and edit the service providers array in the app config.