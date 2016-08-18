import nltk


def main():
    nltk_deps = ['punkt', 'averaged_perceptron_tagger']
    print 'Checking nltk deps...'
    map(nltk.download, nltk_deps)
    print 'nltk deps done'

if __name__ == '__main__':
    main()
