        ++ it;
​
        if ( std::isdigit ( *it ) )
        {
            multiply ( result, parse_repetitions ( it, end ) );
        }
​
        return result;
    }
​
    std::map<std::string, int> parse_molecule ( std::string::const_iterator it, const std::string::const_iterator end )
    {
        std::map<std::string, int> result;
        while ( it != end )
        {
            auto consumed = it;
            if ( *it == '(' )
            {
                merge_atoms ( result, parse_repeated_group ( it, end ) );
            }
            else if ( std::isupper ( *it ) )
            {
                merge_atoms ( result, parse_atom_group ( it, end ) );
            }
            else
            {
                std::cerr << "parse error at index " << std::distance ( parse_start, it ) << ", expected '(' or upper case, got '" << (*it) << "'" << std::endl;
                break;
            }
        }
​
        return result;
    }
​
public:
    std::string countOfAtoms(const std::string & formula)
    {
        std::string result;
        parse_start = formula.cbegin ();
​
        for ( auto const & [ key, value ] : parse_molecule ( parse_start, formula.cend () ) )
        {
            result += key + ( value > 1 ? std::to_string ( value ) : "" );
        }
        return result;
    }
};
